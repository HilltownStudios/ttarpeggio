# TTArpeggio TTRPG Digital Library System

TTArpeggio is a standards-compliant tabletop roleplaying materials digital library system. Its main goal is to make managing your TTRPG files as easy as possible. Don't just put your files in folders on your hard drive and hope for the best.

The impetus behind this system is that while there are several ebook capable digital library systems (e.g., Calibre), they are general purpose systems that take in all sorts of book-like contents, but not, say, images and other non-book materials that might come packaged with TTRPGs. This system looks at what might be bundled with TTRPGs, such as maps, inspiration images, soundtracks, etc., and provides a first-class storage, search, and retrieval platform for them.

## Architecture
1. Python FastAPI backend with fully documented API via Swagger
2. Choice of file storage (local, S3, etc., via plugins)
3. Fast embedded database (DuckDB)
4. Deduplication via checksum
5. Vue 3 frontend
6. Oauth2 authentication
7. (open question) Packaged as a standalone app that doesn't require hosting??

## Metadata
1. Standards-based (e.g., MARC21, Dublin Core serializable)
2. Fetch from known sources, such as RPGGeek, or other friendly instances (e.g., via OAI-PMH)
3. File versioning
4. NB: Separate metadata record and files, but no metadata record without a file, and no files without associated metadata records.

## Features (Incomplete List)
1. List TTRPG materials
2. Search, sort, filter, and facet materials using controlled vocabularies and free text metadata search
3. (In consideration) Full-text PDF search
4. Upload TTRPG material files (attach to existing record or create a new record)
5. Edit and delete files and metadata
6. Web-based access to records; open files in a configured reader or download if permissions allow
7. Role-based access to materials, including allowing remote submission, selective read access by collection, and download.
8. Bulk import of existing folders, using folder structure, file names, and embedded PDF metadata to build records.
9. Users management to control access
10. Single- or multi-user modes, with ease of switching