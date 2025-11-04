# features/hooks/tag_hooks.py
HOOK_REGISTRY = {"before": {}, "after": {}}


def register_tag(tag_name, when="before"):
    def decorator(func):
        HOOK_REGISTRY[when][tag_name] = func
        return func

    return decorator
