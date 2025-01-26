import matplotlib.pyplot as plt
import os
import platform

def clear_console():
    # Check for the operating system and clear accordingly
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def plot(scores, mean_scores):
    clear_console()  # Clear the console screen

    # Plotting code
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores, label='Scores')
    plt.plot(mean_scores, label='Mean Scores')
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.legend(loc='upper left')

    # Use plt.pause() to allow the game to continue running while the plot is visible
    plt.pause(0.1)  # Small pause to allow the plot to be updated without blocking execution
    plt.clf()  # Clear the figure to avoid accumulation of multiple plots
