import lexer


def main():
    content = lexer.get_file_content()
    lexer.scan_content(content)


if __name__ == "__main__":
    main()
