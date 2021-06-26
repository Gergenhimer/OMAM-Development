import json

class OMAMTraits():

    def __init__(self):
        # stores the indices of traits in the matrix in a dict
        # trait names are used as keys
        self.traits = dict()
        # stores lists of all traits included in each group in a dict
        # group names are used as keys
        self.groups = dict()
        self.nextFreeIndex = 0  # start indexing at 0
        self.checksum = 0

    def JSONImport(self, filename):
        """ imports the definition of traits and groups from the specified file """
        with open(filename, 'r') as file:
            resource = json.load(file)
        # load traits into data structure
        for trait in list(resource['Traits']):
            # TODO: add alias support, or drop it entirely
            self.addTrait(trait)
        # add/expand trait groups in data structure
        for group in list(resource['Groups']):
            # assumes resource['Group'] is a dict filled with lists (of traits)
            self.addGroup(group, resource['Groups'][group])
        self.updateChecksum()

    def JSONExport(self, filename):
        """ exports the definition of traits and groups to the specified file all other data is unchanged """
        try: 
            with open(filename, 'r') as file:
                resource = json.load(file)
        except(FileNotFoundError):
            resource = dict()
        # add/replace trait list
        resource['Traits'] = list(self.traits)
        # add/replace group list
        resource['Groups'] = self.groups
        # rewrite file
        with open(filename, 'w') as file:
            json.dump(resource, file)

    def addTrait(self, traitName, alias = None):
        if traitName not in self.traits:
            # get an index for the new trait
            if alias in self.traits:
                # use the index of the alias
                index = self.traits[alias]
            else:
                index = self.nextFreeIndex
                self.nextFreeIndex = self.nextFreeIndex + 1
            # add the new trait to the data structure
            self.traits[traitName] = index            

    def addGroup(self, groupName, traits=None):
        """ Adds traits to a group, creating a new group if it does not exist"""
        if groupName not in self.groups:
            # add it as a key
            self.groups[groupName] = list()
        # add traits to the list - does not check if they have an index
        if traits is not None:
            for quirk in traits:
                if quirk not in self.groups[groupName]:
                    self.groups[groupName].append(quirk)
            # sort the list ?

    def updateChecksum(self):
        """ Generates a checksum for this configuration of traits and groups """
        pass




if __name__ == '__main__':
    traits = OMAMTraits()
    # add a few opposing traits
    traits.addTrait("kind")
    traits.addTrait("cruel")
    traits.addTrait("paranoid")
    traits.addTrait("trusting")
    traits.addTrait("honest")
    traits.addTrait("deceitful")
    # add a couple of groups
    traits.addGroup('intrigue', ['cruel', 'paranoid', 'deceitful'])
    traits.addGroup('diplomacy')
    traits.addGroup('diplomacy', ['kind', 'trusting', 'honest'])
    # save to a json file
    traits.JSONExport('test1.json')

