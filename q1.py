
def swap_case(text, n):
    
    text = text.replace(',', 'TEMP').replace('.', ',').replace('TEMP', '.')
    
    if n < len(text):
        text = text[:n].lower() + text[n:].upper()
    else:
        text = text.lower() 

    return text


text = input("Enter text\n")
N = int(input("Enter N\n"))


output = swap_case(text, N)
print(output)


#Yes, Real time monitoring, Immediate alerts.
#N = 6





