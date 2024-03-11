#define NONE(...)
#define REGISTRY(type, name, ...) void type##_##name_update() {}; \
    void type##_##name_init() {};
#define class(type,name) REGISTRY(type,name) NONE
typedef void* Actor;

class(Actor, MyActor)( 
    void update(Actor self) {
        printf("MyActor update\n");
    }
)