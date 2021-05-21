{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 초\n",
      "[[3, 0]]\n",
      "1 초\n",
      "[[2, 0], [9, 1]]\n",
      "2 초\n",
      "[[1, 0], [9, 1], [6, 2]]\n",
      "3 초\n",
      "[[0, 0], [9, 1], [6, 2]]\n",
      "4 초\n",
      "[[5, 2], [9, 1]]\n",
      "5 초\n",
      "[[4, 2], [9, 1]]\n",
      "6 초\n",
      "[[3, 2], [9, 1]]\n",
      "7 초\n",
      "[[2, 2], [9, 1]]\n",
      "8 초\n",
      "[[1, 2], [9, 1]]\n",
      "9 초\n",
      "[[0, 2], [9, 1]]\n",
      "10 초\n",
      "[[8, 1]]\n",
      "11 초\n",
      "[[7, 1]]\n",
      "12 초\n",
      "[[6, 1]]\n",
      "13 초\n",
      "[[5, 1]]\n",
      "14 초\n",
      "[[4, 1]]\n",
      "15 초\n",
      "[[3, 1]]\n",
      "16 초\n",
      "[[2, 1]]\n",
      "17 초\n",
      "[[1, 1]]\n",
      "18 초\n",
      "[[0, 1]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import heapq\n",
    "#SJF scheduling is optimization scheduling\n",
    "def solution(jobs):\n",
    "    num = len(jobs)\n",
    "    q = []\n",
    "    i = 0\n",
    "    waiting_time = []\n",
    "    while(True):\n",
    "        print(i,'초')\n",
    "        for job in jobs:\n",
    "            if i == job[0]:\n",
    "                heapq.heappush(q, [job[1],job[0]])\n",
    "            else:\n",
    "                jobs.pop(0)\n",
    "                break\n",
    "        print(q)\n",
    "        if q[0][0]!=0:\n",
    "            q[0][0] -= 1\n",
    "        elif q[0][0]==0:\n",
    "            \n",
    "            waiting_time.append(i-q[0][1])\n",
    "            a = heapq.heappop(q)\n",
    "            if q:\n",
    "                q[0][0] -= 1\n",
    "        if not q:\n",
    "            break\n",
    "        i += 1\n",
    "    return int(sum(waiting_time)/num)\n",
    "\n",
    "solution([[0, 3], [1, 9], [2, 6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
