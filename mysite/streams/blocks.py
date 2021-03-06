# """Streamfields live in here"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True,help_text="Add a title")
    text = blocks.TextBlock(required=True,help_text="Add text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label=  "Title & Text"

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True,help_text="Add a title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image",ImageChooserBlock(required=True)),
                ("title",blocks.CharBlock(required=True, max_length=40)),
                ("text",blocks.TextBlock(required=True,max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label=  "Cards"
    


class RichTextBlock(blocks.RichTextBlock):
    """ All Features Included """
    
    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label=  "Full Richtext"

class SimpleRichTextBlock(blocks.RichTextBlock):
    """ Limited Features Included """
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]
        
    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label=  "Simple Richtext"

class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.TextBlock(required=True,features=["bold","italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True,max_length = 40, default=  "Learn More")

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label=  "Call To Action"
    