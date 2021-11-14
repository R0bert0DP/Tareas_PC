#Luis Roberto Diaz Pineda

import argparse
import detectEnglish as traductor

if __name__ == "__main__":
    description = "Cifrado, descifrado y crackeado de mensajes"
    parser = argparse.ArgumentParser(description="Tarea E12 C.D.C. Cesar",

                                 epilog=description,

                                 formatter_class=argparse.RawDescriptionHelpFormatter)
                                 
    parser.add_argument('-modo', choices=['cifrado', 'descifrado', 'crackeo'] ,
                          help='Elegir un modo para saber la utilidad del codigo',
                          required=True)
    parser.add_argument('-msj', type=str,
                        help='Mensaje a cifrar/descifrar',
                        default = "No escojiste un mensaje :(")
    parser.add_argument('-clave', type=str,
                        help='Uso: saber la base de la palabra a cifrar/descifrar',
                        default="hola")
    params = parser.parse_args()
    msj = (params.msj)
    clave = (params.clave)
    modo = (params.modo)


def cif_C(clave, msj):
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in msj:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key

            #print(translatedIndex)
        
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    print()
    print("Este es su mensaje:")
    print(translated)


def desc_C(clave, msj):
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in msj:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            #print(translatedIndex)
        
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print()
    print("Este es su mensaje:")
    print(translated)


def crack_C(msj):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        translated = ''

        # The rest of the program is almost the same as the original program:
        # Loop through each symbol in `message`:
        for symbol in msj:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wrap-around:
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol

        # Display every possible decryption:
        if traductor.isEnglish(translated):
            print()
            print('Key #%s: %s' % (key, translated))
            print("mensaje en español")
            #response = input('>')

            #if response.strip().upper():
                #return translated


if modo == 'cifrado':
  cif = cif_C(clave, msj)
  print(cif)
elif modo == 'descifrado':
  desc = desc_C(clave, msj)
  print(desc)
elif modo == 'crackeo':
  crack = crack_C(msj)
  print(crack)
else:
  print("Esta no es una opción :(")

