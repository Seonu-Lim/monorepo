from langchain_core.pydantic_v1 import BaseModel, Field
from typing_extensions import Optional, TypedDict


class GraphState(TypedDict):
    user_question: str
    user_character: str
    ai_character: str
    documents: list[str]
    search_conversation: Optional[str]
    character_conversation: Optional[str]
    generation: str
    num_retrievals: int


class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )


class GradeAnswer(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    answer_check: str = Field(
        description="The answer is correct in the context of the conversation, 'yes' or 'no'"
    )