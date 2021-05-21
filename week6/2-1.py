{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mirkovC4nizCC44\n",
      "C4\n",
      "mirkovniz\n"
     ]
    }
   ],
   "source": [
    "n = input()\n",
    "m = input()\n",
    "queue = []\n",
    "queue2 = []\n",
    "\n",
    "result=''\n",
    "for i in range(len(n)):\n",
    "    queue.append(n[i])\n",
    "for i in range(len(m)):\n",
    "    queue2.append(m[i])\n",
    "for i in range(len(queue)):\n",
    "    a = queue.pop(0)\n",
    "    if a not in stack2:\n",
    "        result += a\n",
    "if len(result)==0:\n",
    "    print(\"FRULA\")\n",
    "else:\n",
    "    print(result)"
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
