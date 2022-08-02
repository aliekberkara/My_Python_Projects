class Query:
    def __init__(self, value = None, order = None):
        self.list = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                    ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                    ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]
        
        if not value and not order:
            l = self.list
        else:
            l = [li for li in self.list if value == li[order]]
        
        for i in l:
            print(*i, sep=', ')
        
    
    @classmethod
    def fromIsbn(cls, isbn):
        cls(isbn, 0)
    
    @classmethod
    def fromWriter(cls, writer):
        cls(writer, 1)
    
    @classmethod
    def fromArtifact(cls, artifact):
        cls(artifact, 2)
    
    @classmethod
    def fromPublisher(cls, publisher):
        cls(publisher, 3)


Query.fromIsbn("9789753424080")