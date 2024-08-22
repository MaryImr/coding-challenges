from curses import echo
import click
import sys

@click.command()
@click.argument("filename", nargs = -1, type=click.Path(exists=True))
@click.option('-c', "count_bytes", is_flag=True, help="total number of bytes in the file")
@click.option('-l', "count_lines", is_flag=True, help="total number of lines in the file")
@click.option('-w', "count_words", is_flag=True, help="total number of words in the file")
@click.option('-m', "count_chars", is_flag=True, help="total number of characters in the file, output matched -c if locale does not support multibyte characters")

def stats(filename, count_bytes, count_lines, count_words, count_chars):
    file_data = getFileData(filename)
    if filename == ():
        display_name = ''
    else:
        display_name = filename[0]

    if count_bytes:
        filesize_in_bytes = bytesInFile(file_data)
        click.echo(f'{filesize_in_bytes} {display_name}')
    elif count_lines:
        total_lines = linesInFile(file_data)
        click.echo(f'{total_lines} {display_name}')
    elif count_words:
        total_words = wordsInFile(file_data)
        click.echo(f'{total_words} {display_name}')
    elif count_chars:
        total_chars = charsInFile(file_data)
        click.echo(f'{total_chars} {display_name}')
    elif not (count_bytes or count_lines or count_words or count_chars):
        filesize_in_bytes = bytesInFile(file_data)
        total_lines = linesInFile(file_data)
        total_words = wordsInFile(file_data)
        click.echo(f'{total_lines} {total_words} {filesize_in_bytes} {display_name}')

def bytesInFile(file_data):
    filesize_in_bytes = 0
    for line in file_data:
        filesize_in_bytes += len(line)

    return filesize_in_bytes

def linesInFile(file_data):
    total_lines = 0
    for line in file_data:
        total_lines += 1
    return total_lines

def wordsInFile(file_data):
    total_words = 0
    for line in file_data:
        total_words += len(line.split())

    return total_words

def charsInFile(file_data):
    total_chars = 0
    for line in file_data:
        total_chars += len(line.decode())

    return total_chars

def getFileData(filename):
    if filename == ():
        file_data = sys.stdin.buffer
    else:
        with open(filename[0], 'rb') as fp:
            file_data = fp.readlines()

    return file_data

if __name__ == "__main__":
    stats()