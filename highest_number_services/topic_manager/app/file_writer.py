class FileWriter:
    def write_line(self, line, filename="output.txt"):
        with open(filename, mode="wt") as file:
            file.write(line)
