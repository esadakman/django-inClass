from rest_framework import permissions
# ! student infolarının admin ve oluşturulan kişi tarafından CRUD'lanamilmesi için permission oluşturduk
class IsAdminorReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user.is_staff)
        
    
class IsAddedByUserorReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        else:
            # ? oluşturan kişi veya adminin datayı CRUD işlemi yapabilmesi için =>  
            # return obj.user == request.user or request.user.is_staff
            # ? sadece oluşturan kişi CRUD işlemi yapabilmesi için =>  
            return obj.user == request.user 