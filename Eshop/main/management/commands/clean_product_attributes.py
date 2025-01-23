from main.models import ProductAttribute
from django.db.models import Count

# Find duplicates
duplicates = (
    ProductAttribute.objects.values('product', 'color', 'size')
    .annotate(dup_count=Count('id'))
    .filter(dup_count__gt=1)
)

for duplicate in duplicates:
    product_id = duplicate['product']
    color_id = duplicate['color']
    size_id = duplicate['size']

    # Delete all but one
    duplicate_records = ProductAttribute.objects.filter(
        product_id=product_id, color_id=color_id, size_id=size_id
    )
    first_record = duplicate_records.first()
    duplicate_records.exclude(id=first_record.id).delete()

print("Duplicate cleanup completed.")
