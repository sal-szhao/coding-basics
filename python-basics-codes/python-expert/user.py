from library import Base

class Derived(Base):
    def Bar(self):
        return self.foo()