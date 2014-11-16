#include <nan.h>

NAN_METHOD(Open) {
	int master = 0, slave = 0;
	NanScope();
	v8::Handle<v8::Object> ret = NanNew<v8::Object>();
	ret->Set(NanNew<v8::String>("master"), NanNew<v8::Integer>(master));
	ret->Set(NanNew<v8::String>("slave"), NanNew<v8::Integer>(slave));
	NanReturnValue(ret);
}

NAN_METHOD(Resize) {
	NanScope();
	NanReturnUndefined();
}

void Init(v8::Handle<v8::Object> exports) {
	NODE_SET_METHOD(exports, "open", Open);
	NODE_SET_METHOD(exports, "resize", Resize);
}

NODE_MODULE(pty, Init)
