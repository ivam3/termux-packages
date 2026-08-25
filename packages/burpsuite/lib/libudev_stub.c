/*
 * libudev stub for Termux (Android/Bionic).
 *
 * Burp Suite uses com.sun.jna.platform.linux.Udev (jna-platform), which
 * calls Native.load("udev") and invokes the udev_* API to enumerate
 * block devices and CPU topology. Android has no udev, so this stub
 * provides the same symbols returning safe values (no devices, no
 * system info) so JNA initializes Udev.INSTANCE successfully and OSHI
 * falls back to /proc-based discovery.
 */

#include <stddef.h>

typedef struct udev_stub udev_stub;
typedef struct udev_device_stub udev_device_stub;
typedef struct udev_enumerate_stub udev_enumerate_stub;
typedef struct udev_list_entry_stub udev_list_entry_stub;

struct udev_stub { char x; };
struct udev_enumerate_stub { char x; };

/* Opaque objects; only their addresses matter to JNA (PointerType). */
static udev_stub             stub_udev;
static udev_enumerate_stub   stub_enumerate;

void *udev_new(void) {
    return &stub_udev;
}

void *udev_ref(void *udev) {
    return udev;
}

void *udev_unref(void *udev) {
    return udev;
}

void *udev_device_new_from_syspath(void *udev, const char *syspath) {
    return NULL;
}

void *udev_enumerate_new(void *udev) {
    return &stub_enumerate;
}

void *udev_enumerate_ref(void *udev_enumerate) {
    return udev_enumerate;
}

void *udev_enumerate_unref(void *udev_enumerate) {
    return udev_enumerate;
}

int udev_enumerate_add_match_subsystem(void *udev_enumerate, const char *subsystem) {
    return 0;
}

int udev_enumerate_scan_devices(void *udev_enumerate) {
    return 0;
}

void *udev_enumerate_get_list_entry(void *udev_enumerate) {
    return NULL;
}

void *udev_list_entry_get_next(void *udev_list_entry) {
    return NULL;
}

const char *udev_list_entry_get_name(void *udev_list_entry) {
    return NULL;
}

void *udev_device_ref(void *udev_device) {
    return udev_device;
}

void *udev_device_unref(void *udev_device) {
    return udev_device;
}

void *udev_device_get_parent(void *udev_device) {
    return NULL;
}

void *udev_device_get_parent_with_subsystem_devtype(void *udev_device, const char *subsystem, const char *devtype) {
    return NULL;
}

const char *udev_device_get_syspath(void *udev_device) {
    return NULL;
}

const char *udev_device_get_sysname(void *udev_device) {
    return NULL;
}

const char *udev_device_get_devnode(void *udev_device) {
    return NULL;
}

const char *udev_device_get_devtype(void *udev_device) {
    return NULL;
}

const char *udev_device_get_subsystem(void *udev_device) {
    return NULL;
}

const char *udev_device_get_sysattr_value(void *udev_device, const char *sysattr) {
    return NULL;
}

const char *udev_device_get_property_value(void *udev_device, const char *property) {
    return NULL;
}