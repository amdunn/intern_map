function find_where_lives() {
    /* Not 100% sure what the _4_ug box is, but this seems to work */
    var boxes = $('div[role="article"] li[class="_4_ug"]');
    var result = null;

    if (boxes.length == 0) {
        throw "fail: no boxes found";
    }

    boxes.each(function (idx) {
        var html = this.innerHTML;

        if (html.search("Lives in") != -1 &&
            result === null) {
            result = html;
        }
    });

    if (!(result === null)) {
        return result;
    }

    throw "fail: no lives in box found";
}

$(document).ready(function() {
    /* This is the way we communicate the result to outside Chrome -
     * we can find the value via accessing Chrome local storage (at
     * least in Linux it's a sqlite3 database).
     *
     * XXX: Is there a better way to do this?
     */
    var where_lives = 'Fail';

    try {
        where_lives = find_where_lives();
    } catch(err) {
    }

    localStorage.setItem('XXX', where_lives);

    /* hack to close this tab */
    window.open('', '_self', '');
    window.close();
});
