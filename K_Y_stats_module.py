{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3972efad-697d-4d70-9b8b-1d8eb72486ee",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import math\n",
    "def calculate_mean(numbers):\n",
    "    if not numbers:\n",
    "        return None\n",
    "    return sum(numbers) / len(numbers)\n",
    "def calculate_variance(numbers):\n",
    "    if not numbers:\n",
    "        return None\n",
    "    mean = calculate_mean(numbers)\n",
    "    return sum((x - mean) ** 2 for x in numbers) / len(numbers)\n",
    "\n",
    "def calculate_std_deviation(numbers):\n",
    "    variance = calculate_variance(numbers)\n",
    "    if variance is None:\n",
    "        return None\n",
    "    return math.sqrt(variance)\n",
    "\n",
    "def calculate_std_error(numbers):\n",
    "    std_dev = calculate_std_deviation(numbers)\n",
    "    if std_dev is None:\n",
    "        return None\n",
    "    return std_dev / math.sqrt(len(numbers))\n",
    "\n",
    "def calculate_z_score(numbers, new_value):\n",
    "    mean = calculate_mean(numbers)\n",
    "    std_dev = calculate_std_deviation(numbers)\n",
    "    if std_dev is None:\n",
    "        return None\n",
    "    return (new_value - mean) / std_dev"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "634da42c-477b-4c77-b870-f5a57ab511f2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
