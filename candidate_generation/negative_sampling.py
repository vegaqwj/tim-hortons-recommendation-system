
import random

def generate_negative_samples(user_history, all_items, n=2):

    samples = []

    for user, items in user_history.items():

        for pos in items:

            samples.append((user, pos, 1))

            for _ in range(n):

                neg = random.choice(all_items)

                while neg in items:
                    neg = random.choice(all_items)

                samples.append((user, neg, 0))

    return samples
