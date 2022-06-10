from logging import root
import os

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        self.altura = 0

    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)

    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)
    
def altura(a):
    # condición base cuando el árbol binario está vacío
        if a == None:
            return 0
        return max(altura(a.left), altura(a.right)) + 1
 
    # función para comprobar si el árbol está equilibrado en altura o no
def checkbalance(a):
     
    # Condicion Base
        if a == None:
         return True
 
    # para la altura del subárbol izquierdo y derecho
        l = altura(a.left)
        r = altura(a.right)
 
    # los valores permitidos para (l - r) son 1, -1, 0
        if (abs(l - r) <= 1) and checkbalance(a.left) is True and checkbalance( a.right) is True:
            return True
 
    # si llegamos aquí significa que el árbol no es
    # árbol equilibrado de altura
        return False

tree = arbol()

while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Factor de equilibrio \n7.-Salir \n\nElige una opcion -> ")

    if opc == '1':
        nodo = input("\nIngresa el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
        else:
            print("\nIngresa solo digitos...")
    elif opc == '2':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ",
                      tree.buscar(nodo, tree.root), " si existe...")
        else:
            print("\nIngresa solo digitos...")
    elif opc == '6':
        if checkbalance(tree.root):
            print("El arbol esta balanceado")
        else:
            print("El arbol no esta balanceado")

    elif opc == '7':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()

#ejemplos para evaluar el factor de equilibrio Arbol AVL

#20,10,40,5,15,50,45,30 balanceado es AVL VALIDO
#6,2,8,4,1,7,3  balanceado, es AVL
#20,10,40,5,15,50,45  NO ES UN arbol avl valido (no balanceado)
#20,10,5,15  NO ES UN arbol avl valido (no balanceado)