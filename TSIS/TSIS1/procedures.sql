-- procedures.sql
-- Stored procedures and functions for PhoneBook TSIS1

-- 1. Procedure: add_phone
-- Adds a new phone number to an existing contact by name
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE name = p_contact_name;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact "%" not found', p_contact_name;
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (v_contact_id, p_phone, p_type)
    ON CONFLICT (contact_id, phone) DO NOTHING;
END;
$$;


-- 2. Procedure: move_to_group
-- Moves a contact to a group; creates the group if it does not exist
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_group_id INTEGER;
BEGIN
    INSERT INTO groups(name)
    VALUES (p_group_name)
    ON CONFLICT (name) DO NOTHING;

    SELECT id INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE name = p_contact_name;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Contact "%" not found', p_contact_name;
    END IF;
END;
$$;


-- 3. Function: search_contacts
-- Searches contacts by name, surname, email, or any phone number
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id         INTEGER,
    name       VARCHAR,
    surname    VARCHAR,
    email      VARCHAR,
    birthday   DATE,
    group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id,
        c.name,
        c.surname,
        c.email,
        c.birthday,
        g.name AS group_name
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE
        c.name    ILIKE '%' || p_query || '%'
        OR c.surname ILIKE '%' || p_query || '%'
        OR c.email   ILIKE '%' || p_query || '%'
        OR p.phone   ILIKE '%' || p_query || '%';
END;
$$;


-- 4. Function: get_contacts_paginated
-- Returns contacts with pagination support (LIMIT / OFFSET)
CREATE OR REPLACE FUNCTION get_contacts_paginated(
    p_limit  INTEGER,
    p_offset INTEGER
)
RETURNS TABLE (
    id         INTEGER,
    name       VARCHAR,
    surname    VARCHAR,
    email      VARCHAR,
    birthday   DATE,
    group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name,
        c.surname,
        c.email,
        c.birthday,
        g.name AS group_name
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$;
