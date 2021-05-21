{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 7]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def solution(gems):\n",
    "    answer = []\n",
    "    size = len(set(gems))\n",
    "    dic = {gems[0]: 1}\n",
    "    temp = [1, len(gems)]\n",
    "    start, end = 0, 0\n",
    "    while(start<len(gems) and end < len(gems)):\n",
    "        if len(dic) != size:\n",
    "            end += 1\n",
    "            if end >= len(gems):\n",
    "                break\n",
    "            dic[gems[end]] = dic.get(gems[end], 0)+1\n",
    "        else: \n",
    "            if end - start < temp[1] - temp[0]:\n",
    "                temp = [start + 1, end + 1]\n",
    "            if dic[gems[start]] == 1:\n",
    "                del dic[gems[start]]\n",
    "            else:\n",
    "                dic[gems[start]] -= 1\n",
    "            start += 1\n",
    "    return temp\n",
    "\n",
    "a=solution([\"DIA\", \"RUBY\", \"RUBY\", \"DIA\", \"DIA\", \"EMERALD\", \"SAPPHIRE\", \"DIA\"])\n",
    "a"
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
