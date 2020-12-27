from shutil import rmtree
from tempfile import mkdtemp
from pathlib import Path
from multiprocessing import Process, Pool, RLock
from tqdm import tqdm
from core import Canvas


class RayTracer():
    def __init__(self):
        pass

    def render(self, camera, world):
        """render world into canvas"""

        image = Canvas(camera.horizontal_size_px, camera.vertical_size_px)

        for y in range(camera.vertical_size_px):
            for x in range(camera.horizontal_size_px):
                ray = camera.ray_for_pixel(x, y)
                color = world.color_at(ray)
                image.set_pixel(x, y, color)

        return image

    def render_part(self, pid, camera, world, hmin, hmax, part_file):
        """ """
        tqdm_text = "#" + "{}".format(pid).zfill(3)

        image = Canvas(camera.horizontal_size_px, hmax - hmin)

        pbar = tqdm(total=hmax - hmin, desc=tqdm_text, position=pid)
        for y in range(hmin, hmax):
            for x in range(camera.horizontal_size_px):
                ray = camera.ray_for_pixel(x, y)
                color = world.color_at(ray)
                image.set_pixel(x, y - hmin, color)
            pbar.update(1)

        with open(part_file, 'w') as outf:
            outf.write(image.pixels_to_string())

    def write_ppm_header(self, result_file_obj, camera):
        result_file_obj.write( \
"""P3
{width} {height}
255
""".format(width=camera.horizontal_size_px, height=camera.vertical_size_px))

    def render_multi_process(self, camera, world, result_file_obj):
        """render world into canvas using multiple processes"""

        process_ranges = self.__split_range(camera.vertical_size_px, 8)
        temp_dir = Path(mkdtemp())
        temp_file_pattern = "part-{}.ppm"
        # processes = []

        # write PPM file header
        self.write_ppm_header(result_file_obj, camera)

        try:
            print('create process pool')
            pool = Pool(processes=8,
                        initargs=(RLock(), ),
                        initializer=tqdm.set_lock)

            print('assemble argument list')
            argument_list = [(hmin, hmax,
                              temp_dir / temp_file_pattern.format(hmin))
                             for hmin, hmax in process_ranges]

            print('start jobs')
            jobs = [
                pool.apply_async(self.render_part,
                                 args=(pid, camera, world, arg[0], arg[1],
                                       arg[2]))
                for pid, arg in enumerate(argument_list)
            ]

            print('pool close')
            pool.close()

            print('wait for jobs')
            results = [job.get() for job in jobs]
            # Important to print these blanks
            print("\n" * (len(argument_list) + 1))

            # for hmin, hmax in process_ranges:
            #     part_file = temp_dir / temp_file_pattern.format(hmin)
            #     processes.append(
            #         Process(target=self.render_part,
            #                 args=(camera, world, hmin, hmax, part_file)))

            # for p in processes:
            #     p.start()

            # for p in processes:
            #     p.join()

            for hmin, _ in process_ranges:
                part_file = temp_dir / temp_file_pattern.format(hmin)
                result_file_obj.write(open(part_file, "r").read())

        finally:
            # print("finished")
            rmtree(temp_dir)

    def __split_range(self, count, parts):
        q, r = divmod(count, parts)
        print(f"q={q}, r={r}")
        splits = [(i * q + min(i, r), (i + 1) * q + min(i + 1, r))
                  for i in range(parts)]
        print(f"splits={splits}")
        return splits
