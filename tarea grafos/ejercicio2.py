class GeneroMusical:
    def __init__(self, genero):
        self.genero = genero
        self.artistas = []
        
    def agregar_artista(self, artista):
        self.artistas.append(artista)
        
    def mostrar_genero(self):
        print(f"Género: {self.genero}")
        for artista in self.artistas:
            print(f"- {artista}")

rock = GeneroMusical('Rock')
rock.agregar_artista('Tokio Hotel')
rock.agregar_artista('Sleeping with sirens')
rock.agregar_artista('Likin Park')
rock.mostrar_genero()