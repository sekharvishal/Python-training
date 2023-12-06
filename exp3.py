class namme:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def get_name(self,name):
         self.name=name;
    def set_name(self,name):
        return self.name;

v=namme("__vishal__",29);
s=namme("gowtham",23)

print(v.name);
print(v.age);


namme.set_name(v,"vishal")
v.get_name("vishal")
v.age=20;
print(v.name);
print(v.age);
print(s.name);
print(s.age);
