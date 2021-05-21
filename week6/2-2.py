{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "def solution(priorities, location):\n",
    "    answer = 0\n",
    "    queue = []\n",
    "    \n",
    "    for i, item in enumerate(priorities):\n",
    "        queue.append([item,i])\n",
    "    while(True):\n",
    "        max_num = max(queue)[0]\n",
    "        a = queue.pop(0)\n",
    "        if a[0]==max_num: # minqueue를 따로 관리하도록해도 가능\n",
    "            answer += 1\n",
    "            if a[1] == location:\n",
    "                break\n",
    "        else:\n",
    "            queue.append(a)\n",
    "    return answer\n",
    "print(solution([1, 1, 9, 1, 1, 1], 0))"
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
