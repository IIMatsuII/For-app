from tqdm import tqdm
from time import sleep
import random

print("Начало загрузки....\n ")

for i in tqdm(range(100), colour="green"):
    sleep(random.uniform(0.01, 0.1))

print("\nЗагрузка завершена.... ")
