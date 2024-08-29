import dlib

# Exemplo simples para testar o dlib
print("dlib version:", dlib.__version__)

detector = dlib.get_frontal_face_detector()
print("Face detector loaded successfully:", detector is not None)
