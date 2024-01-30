from datetime import datetime
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os

# Dieser Code soll nur den Code zeigen der ein Bild erstellt und in einem Ordner speichert.

# Überprüfe, ob eine Person im Bild erkannt wurde
if 'person' in label:
    # Bekommt das Heutige Datum
    datetime = datetime.today().strftime('%Y-%m-%d')
    # Erstellen Sie einen Dateinamen für das Bild
    filename = f'Erkennung{datetime}.jpg'
    # Erstellen Sie einen Ordner namens 'persons', wenn er nicht existiert
    if not os.path.exists('Erkennung'):
        os.mkdir('Erkennung')
    # Speichern Sie das Bild im Ordner 'persons' mit dem Dateinamen
    cv2.imwrite(os.path.join('persons', filename), output_image)

# Zeigen Sie das Bild in einem Fenster an
cv2.imshow('output', output_image)

# Beenden Sie die Schleife, wenn die Taste 'q' gedrückt wird
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
