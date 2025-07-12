
---

### ✅ 3. `update.md` — only this content:

```markdown
# Update Book

```python
book = Book.objects.get(author="George Orwell")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
# Output: Nineteen Eighty-Four by George Orwell (1949)
