-- 1. Search contacts by name or phone pattern
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(search_pattern TEXT)
RETURNS TABLE (id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.phone
    FROM contacts c
    WHERE c.first_name ILIKE '%' || search_pattern || '%'
       OR c.phone ILIKE '%' || search_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Paginated query
CREATE OR REPLACE FUNCTION get_contacts_paginated(page_size INT, page_number INT)
RETURNS TABLE (id INT, first_name VARCHAR, phone VARCHAR) AS $$
DECLARE
    calculate_offset INT;
BEGIN
    calculate_offset := (page_number - 1) * page_size;
    RETURN QUERY
    SELECT c.id, c.first_name, c.phone
    FROM contacts c
    ORDER BY c.id
    LIMIT page_size OFFSET calculate_offset;
END;
$$ LANGUAGE plpgsql;