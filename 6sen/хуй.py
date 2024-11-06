import matplotlib.pyplot as plt

def text_to_binary(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    return binary_text

def plot_binary_graph(binary_text):
    binary_values = [int(bit) for bit in binary_text.split()]
    plt.figure(figsize=(10, 4))
    plt.step(range(len(binary_values)), binary_values, where='post')
    plt.ylim(-0.5, 1.5)
    plt.xlabel('Bit Position')
    plt.ylabel('Bit Value')
    plt.title('Binary Representation of Text')
    plt.grid(True)
    plt.show()

# Пример использования
text = "Hello, World!"
binary_text = text_to_binary(text)
plot_binary_graph(binary_text)