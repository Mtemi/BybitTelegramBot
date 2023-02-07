from flask_marshmallow import Marshmallow

ma = Marshmallow()

class AssetSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("symbol_id", "asset", "size", "side", "price", "usdvalue")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("asset_detail", id="<id>"), "collection": ma.URLFor("assets")}
    )

