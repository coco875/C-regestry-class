#define NONE(...)
#define REGISTRY(type, name, ...) void type##_##name_update() {}; \
    void type##_##name_init() {};
typedef void* Actor;

    void Actor_MyActor_update(Actor self) {
        printf("MyActor update\n");
    }
