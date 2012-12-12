function find_where_lives() {
    var about_box = $('li[class~="about"]');
    if (about_box.length != 1)
        throw "fail: 1";

    /* Lines in profile (e.g. "Lives in ...") */
    var profile_lines = $('span[class="fbProfileBylineLabel"]', about_box[0]);
    if (profile_lines.length == 0)
        throw "fail: 2";

    var result = false;
    profile_lines.each(function() {
        var html = this.innerHTML;

        if (html.search("Lives") != -1) {
            result = html;
            return;
        }
    });

    if (!(result === false))
        return result;

    throw "fail: 3";
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
