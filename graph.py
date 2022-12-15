import matplotlib.pyplot as plt
import csv


def plot_all():
    
  # Read data from CSV file
  input_sizes = []
  greedy_times = []
  dp_times = []
  brute_force_times = []

  with open('output.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # next(reader)  # Skip header row
    for row in reader:
      input_sizes.append(int(row[0]))
      greedy_times.append(float(row[1]))
      dp_times.append(float(row[2]))
      brute_force_times.append(float(row[3]))

  # Create plot
  plt.plot(input_sizes, greedy_times, label='Greedy')
  plt.plot(input_sizes, dp_times, label='DP')
  plt.plot(input_sizes, brute_force_times, label='Brute force')
  plt.xlabel('Input size')
  plt.ylabel('Time (seconds)')
  plt.legend()

  # Save plot to file
  plt.savefig('performance.png')

def plot_dp_greedy():
  # Read data from CSV file
  input_sizes = []
  greedy_times = []
  dp_times = []


  with open('DPvsGreedy.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # next(reader)  # Skip header row
    for row in reader:
      input_sizes.append(int(row[0]))
      greedy_times.append(float(row[1]))
      dp_times.append(float(row[2]))
  

  # Create plot
  plt.plot(input_sizes, greedy_times, label='Greedy')
  plt.plot(input_sizes, dp_times, label='DP')
  plt.xlabel('Input size')
  plt.ylabel('Time (seconds)')
  plt.legend()

  # Save plot to file
  plt.savefig('DPvsGreedy.png')


if __name__ == '__main__':
  # plot_all()
  plot_dp_greedy()