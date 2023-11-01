class Key:
    def __init__(self):
        self.attributes = []
        self.isPrimary = False

    
    def __repr__(self):
        return f"Key: {self.attributes} {'(PRIMARY)' if self.isPrimary else ''}"