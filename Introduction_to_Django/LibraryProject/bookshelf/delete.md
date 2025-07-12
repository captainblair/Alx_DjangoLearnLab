
---

### ✅ 4. `delete.md` — only this content:

```markdown
# Delete Book

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
# Output: <QuerySet []>
