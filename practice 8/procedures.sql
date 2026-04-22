-- 1. Upsert (Insert or Update if name exists)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    INSERT INTO contacts (first_name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (first_name) 
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$ LANGUAGE plpgsql;

-- 2. Bulk Insert using Arrays
CREATE OR REPLACE PROCEDURE insert_many_contacts(p_names TEXT[], p_phones TEXT[])
AS $$
BEGIN
    INSERT INTO contacts (first_name, phone)
    SELECT unnest(p_names), unnest(p_phones)
    ON CONFLICT (first_name) DO NOTHING;
END;
$$ LANGUAGE plpgsql;

-- 3. Delete contact by Name or Phone
CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
AS $$
BEGIN
    DELETE FROM contacts
    WHERE first_name = p_value OR phone = p_value;
END;
$$ LANGUAGE plpgsql;sssssdw