# Data architecture

CONFIRMED requirements: department-isolated operational data and local analytics; governed approved analytical exports into the Owner warehouse. The framework recommendation is Next.js/Vercel with Supabase PostgreSQL/Auth/Storage, subject to actual starter/account verification. The following physical layout is PROPOSED until reviewed through schema contracts.

Department OLTP -> private raw files/extraction snapshots -> staging/quality checks -> local analytical facts/dimensions/marts -> approved export batch -> Owner staging/reconciliation -> enterprise warehouse -> dependent marts/OLAP -> dashboards/KPIs -> management decision.

PostgreSQL schemas can provide logical separation initially; they do not isolate compute. Evaluate separate analytical databases/read replicas as real workload evidence warrants. Do not claim a logically separated schema is physical OLTP/OLAP isolation. Supabase Storage plus source catalogs can supply a bounded raw landing/lake layer; a bucket alone does not implement governance or ETL.

Model normalized OLTP before dimensional reporting. Declare each fact's grain, source, time basis, unit/currency, additive behavior and correction semantics. Distinguish Manga engagement/ad settlement, Anime viewing/subscription cash, Merch receipt/sale/return/supplier payment, and Owner-approved aggregate reports. Use conformed dimensions only at permitted grain; no central raw customer identity/payment credentials/sensitive viewing events.

Star=focused fact/dimensions; snowflake=justified normalized hierarchies; galaxy=multiple facts with shared dimensions. These are modeling patterns, not separate products. Use SCD1 for justified corrections, SCD2 for effective-dated history, SCD3 for an explicit limited previous/current comparison. Never overwrite financial originals as a dimension-cleanup shortcut.

Every pipeline needs a source inventory, source-to-target map, raw retention policy, validation/quarantine, stable native keys, incremental checkpoints, deduplication/retry rules, reconciliation totals, lineage, batch permissions and observable run evidence. No name-only identity merging. Unknown is not zero. Preserve original time zones and define reporting boundaries.

Begin with descriptive verified reports and transparent trend calculations. Big Data, IoT and predictive AI/ML are not automatically required; justify each with actual data, user purpose, privacy and measured need before adding infrastructure or models.
