from tqdm import tqdm, trange
import time

# for i in tqdm([1, 2, 3, 4, 5]):
#     # show progress bar in 5 sections (5/5) and sleep in 0.3 second in between
#     time.sleep(0.3)
#
# for i in trange(10):
#     # show progress bar in 10 sections (10/10) and sleep in 0.3 second in between
#     time.sleep(0.3)

# with tqdm(total=100) as pbar:
#     # progress bar with 100
#     for i in range(10):
#         time.sleep(0.3)
#         # each iteration update 10
#         pbar.update(10)

pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.3)
    pbar.update(10)
pbar.close()
