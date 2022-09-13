from __future__ import absolute_import
import factory
if __name__ == "__main__":
    app2 = factory.create_app()
    app2.run(host="0.0.0.0", port="7000", debug=True)