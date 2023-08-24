class properties():
    
    property_values = {}

    def read_properties_file(self, file_path):
    
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    self.property_values[key.strip()] = value.strip()
        return self.property_values