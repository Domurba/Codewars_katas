#2021-09-16 10:57:31.382000+00:00
"""Your job is working with documents: creating, modifying, and deleting them. It is a very important task, so you must also keep a changelog of performed operations. Updating it manually every time is very tedious, so you decided to automate the job.

You have to do something, so that all the changes done on the `documents` table are reflected in the `documents_changelog` table:
1. On insert copy the new data into the `new_data` column
2. On update copy the previous data into the `old_data` and the new data into the `new_data` columns
3. On delete copy the old data into the `old_data` column
4. If the operation has no new/old data to work with, the respective column should store `NULL`

## Tables

```
--------------------------------------------
|        Table        |   Column    | Type |
|---------------------+-------------+------|
| documents           | id          | int  |
|                     | data        | text |
|---------------------+-------------+------|
| documents_changelog | id          | int  |
|                     | document_id | int  |
|                     | old_data    | text |
|                     | new_data    | text |
--------------------------------------------
```"""

CREATE FUNCTION change_trigger() RETURNS trigger AS $$
        BEGIN
        IF TG_OP = 'INSERT' THEN
        INSERT INTO documents_changelog (document_id, old_data, new_data)
        VALUES (new.id, NULL, NEW.data); return new;
        ELSIF   TG_OP = 'UPDATE' THEN
        INSERT INTO documents_changelog (document_id, old_data, new_data)
        VALUES (new.id, OLD.data, NEW.data);  return new;
        ELSIF   TG_OP = 'DELETE' THEN
        INSERT INTO documents_changelog (document_id, old_data, new_data)
        VALUES (old.id, OLD.data, Null); return old;
        END IF;
        END;
       $$ LANGUAGE 'plpgsql' SECURITY DEFINER; 
CREATE TRIGGER t BEFORE INSERT OR UPDATE OR DELETE ON documents
        FOR EACH ROW EXECUTE PROCEDURE change_trigger();
                