from django.http import HttpResponse
from django.shortcuts import render
def caesar_cipher(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        shift = int(request.POST.get('shift'))
        encrypted_text = encrypt(text, shift)
        return HttpResponse(encrypted_text)
    else:
        return render(request, 'caesar_cipher.html')

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result
