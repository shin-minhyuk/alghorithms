import sys

input = sys.stdin.readline

from queue import PriorityQueue

pq = PriorityQueue()
N = int(input())

for _ in range(N):
  cards = int(input())
  pq.put(cards)

total = 0
while pq.qsize() > 1:
  min_cards_value_1 = pq.get()
  min_cards_value_2 = pq.get()

  pq.put(min_cards_value_1 + min_cards_value_2)
  total += min_cards_value_1 + min_cards_value_2

print(total)