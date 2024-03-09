#define class void
typedef void* Actor;

class MyActor(Actor) {
    void update(Actor self) {
        printf("MyActor update\n");
    }
}