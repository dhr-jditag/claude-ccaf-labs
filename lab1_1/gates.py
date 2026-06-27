from lab1_1.context import TicketContext


class PipelineGateError(Exception):
    """
    Custom exception raised when a step precondition check fails.
    """
    pass


def gate_classification(ctx: TicketContext) -> None:
    """
    Enforces that classification is complete before proceeding.
    """
    if not ctx.classification_complete():
        missing_fields = []
        if ctx.product_area is None:
            missing_fields.append("product_area")
        if ctx.severity is None:
            missing_fields.append("severity")
        if ctx.intent is None:
            missing_fields.append("intent")
        
        raise PipelineGateError(
            f"Classification Gate Failed. Missing fields: {', '.join(missing_fields)}. "
            "Please ensure classification is complete."
        )
    return None


def gate_enrichment(ctx: TicketContext) -> None:
    """
    Enforces that CRM enrichment is complete before proceeding.
    """
    if not ctx.enrichment_complete():
        missing_fields = []
        if ctx.account_tier is None:
            missing_fields.append("account_tier")
        if ctx.sla_tier is None:
            missing_fields.append("sla_tier")
        
        raise PipelineGateError(
            f"Enrichment Gate Failed. Missing fields: {', '.join(missing_fields)}. "
            "Please rerun the CRM Enricher."
        )
    return None


def gate_draft(ctx: TicketContext) -> None:
    """
    Enforces that draft response is created before proceeding.
    """
    if not ctx.draft_complete():
        raise PipelineGateError(
            "Draft Gate Failed. draft_response is None. "
            "Please rerun the Drafter."
        )
    return None
