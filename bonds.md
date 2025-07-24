## 1. Issuer-Instrument Relationships 🏛️➡️📜
This is the most fundamental connection. It links the entity that raises capital to the financial product it created.

(Issuer) -[:ISSUES]-> (Instrument)

Description: A Company, Government, or Municipality (Issuer) issues a Bond or Equity (Instrument).

Example: Reliance Industries Limited -[:ISSUES]-> Equity (RELIANCE.NS). Government of India -[:ISSUES]-> G-Sec Bond (IN071833G).

Properties on Edge: issue_date, offering_amount, lead_underwriter.

(Entity) -[:GUARANTEES]-> (Bond)

Description: A parent company or government entity guarantees the debt of another entity. This is a critical risk relationship.

Example: Tata Sons -[:GUARANTEES]-> Bond XYZ (issued by a subsidiary).

## 2. Market and Trading Relationships 📈
These relationships place the instrument in the context of the wider market.

(Instrument) -[:TRADES_ON]-> (Exchange)

Description: An equity or bond is listed and traded on a specific stock exchange.

Example: Equity (RELIANCE.NS) -[:TRADES_ON]-> National Stock Exchange.

(Instrument) -[:IS_INCLUDED_IN]-> (Index)

Description: The instrument is a constituent of a market index. This is key for performance and market-level questions.

Example: Equity (HDFCBANK.NS) -[:IS_INCLUDED_IN]-> Nifty 50 Index.

(Instrument) -[:DENOMINATED_IN]-> (Currency)

Description: Links an instrument to its trading and settlement currency.

Example: A Masala Bond -[:DENOMINATED_IN]-> INR. Apple Equity -[:DENOMINATED_IN]-> USD.

## 3. Descriptive and Classification Relationships 📊
These relationships categorize and describe issuers and instruments, allowing for powerful filtering and aggregation.

(Issuer) -[:BELONGS_TO]-> (Sector/Industry)

Description: Connects a company to its line of business.

Example: Infosys -[:BELONGS_TO]-> Information Technology Sector.

(Issuer) -[:LOCATED_IN]-> (Country/Region)

Description: Geopolitical classification for an issuer.

Example: Tata Motors -[:LOCATED_IN]-> India.

(Bond) -[:HAS_RATING]-> (CreditRating)

Description: The bond has a specific credit rating assigned by an agency. You can model this further: (CreditRating) -[:ASSIGNED_BY]-> (RatingAgency).

Example: A Corporate Bond -[:HAS_RATING]-> AAA, and (AAA) -[:ASSIGNED_BY]-> (CRISIL).

## 4. Corporate Hierarchy Relationships 🏢
This is a classic graph use case that is very difficult to model in relational databases. It's crucial for understanding ownership and risk concentration.

(Company) -[:PARENT_OF]-> (Company) or (Company) -[:SUBSIDIARY_OF]-> (Company)

Description: Models the ownership structure between corporate entities.

Example: Alphabet Inc. -[:PARENT_OF]-> Google LLC.

By focusing on these relationships, your GraphRAG will be able to answer complex, multi-hop questions like:

"Show me all INR denominated bonds with a AAA rating that were issued by Indian companies in the Automotive sector and are guaranteed by their parent company."

This query would require multiple JOINs and subqueries in SQL but is a straightforward traversal in a graph, making it ideal for retrieval.
